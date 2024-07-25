ARG ROOT_CONTAINER=jupyter/base-notebook:ubuntu-22.04@sha256:0ec801994602a53d3917d0f07ccf4474a1ddf5ae419483b24681a3c42abc4ce5
ARG BASE_CONTAINER=$ROOT_CONTAINER
FROM $BASE_CONTAINER

MAINTAINER Niklas Siemer <n.siemer@mpie.de>

USER root

#removing the default user and the corresponding home directory.
#RUN rm -r /home/$NB_USER
#RUN userdel $NB_USER

#ARG DOCKER_USER="pyiron"
ARG DOCKER_UID="1000"
ARG DOCKER_GID="100"

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    DOCKER_UID=$DOCKER_UID \
    DOCKER_GID=$DOCKER_GID
    # DOCKER_USER=$DOCKER_USER

#ENV HOME=/home/$DOCKER_USER
ENV HOME=/home/$NB_USER


COPY apt.txt /tmp/
# creating account for pyiron_user.
# RUN useradd -m -s /bin/bash -N -u $DOCKER_UID $DOCKER_USER && \
#     chown $DOCKER_USER:$NB_GID $CONDA_DIR && \
#     chmod g+w /etc/passwd

RUN apt-get update -y && \
    xargs -a /tmp/apt.txt apt-get install -y && \
    apt-get clean && \
    rm /tmp/apt.txt

USER $DOCKER_UID
WORKDIR $HOME
ARG PYTHON_VERSION=default

COPY .  ${HOME}/
RUN mamba env update -n base -f ${HOME}/environment.yml && \
    mamba env create --name iuc04 -f ${HOME}/iuc04-demonstrator/binder/environment.yml && \
    mamba env create --name iuc09 -f ${HOME}/iuc09_demonstrator/binder/environment.yml && \
    mamba env create --name iuc17 -f ${HOME}/IUC17_demonstrator_environment/.binder/environment.yml && \
    mamba env create --name iuc17 -f ${HOME}/IUC17_demonstrator_environment/.binder/environment.yml && \
    mamba env create --name exp_wf_demo -f ${HOME}/experimental_workflow_demo/binder/environment.yml && \
    mamba clean --all -f -y && \
    mamba list

WORKDIR ${HOME}/iuc04-demonstrator/
RUN bash binder/download_and_install_dataset.sh


WORKDIR ${HOME}
RUN mv iuc09_demonstrator/binder/.pyiron . && \
    iuc09_demonstrator/pyiron . && \
    chmod u+x pyiron/resources/paraprobe-ranger/bin/run_paraprobe-ranger_1.0.3_mpi.sh && \
    chmod u+x pyiron/resources/paraprobe-ranger/bin/run_paraprobe-ranger_1.0.3.sh && \
    chmod u+x pyiron/resources/paraprobe-distancer/bin/run_paraprobe-distancer_1.0.3_mpi.sh && \
    chmod u+x pyiron/resources/paraprobe-distancer/bin/run_paraprobe-distancer_1.0.3.sh && \
    chmod u+x pyiron/resources/paraprobe-surfacer/bin/run_paraprobe-surfacer_1.0.3_mpi.sh && \
    chmod u+x pyiron/resources/paraprobe-surfacer/bin/run_paraprobe-surfacer_1.0.3.sh && \
    chmod u+x pyiron/resources/paraprobe-tessellator/bin/run_paraprobe-tessellator_1.0.3_mpi.sh && \
    chmod u+x pyiron/resources/paraprobe-tessellator/bin/run_paraprobe-tessellator_1.0.3.sh && \
    chmod u+x pyiron/resources/paraprobe-nanochem/bin/run_paraprobe-nanochem_1.0.3_mpi.sh && \
    chmod u+x pyiron/resources/paraprobe-nanochem/bin/run_paraprobe-nanochem_1.0.3.sh


# Fix permissions on /etc/jupyter as root
USER root
RUN fix-permissions /etc/jupyter/ &&\
    fix-permissions ${HOME} && \
    fix-permissions $CONDA_DIR


USER $DOCKER_UID

WORKDIR $HOME
